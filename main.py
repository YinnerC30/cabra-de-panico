"""
Cabra de pánico — icono en la bandeja del sistema (Windows).
Clic izquierdo en el icono: reproduce cabra_gritando.mp3.
Clic derecho: menú con Salir.
"""

from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtGui import QAction, QIcon
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtWidgets import QApplication, QMenu, QSystemTrayIcon, QMessageBox


def base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent


def resource_path(name: str) -> Path:
    return base_dir() / name


def main() -> int:
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)

    mp3_path = resource_path("cabra_gritando.mp3")
    icon_path = resource_path("cabra.png")

    if not mp3_path.is_file():
        QMessageBox.critical(
            None,
            "Cabra de pánico",
            f"No se encuentra el audio:\n{mp3_path}",
        )
        return 1

    player = QMediaPlayer()
    audio_out = QAudioOutput()
    player.setAudioOutput(audio_out)
    player.setSource(QUrl.fromLocalFile(str(mp3_path.resolve())))

    def play_cabra() -> None:
        player.setPosition(0)
        player.play()

    tray = QSystemTrayIcon()
    if icon_path.is_file():
        tray.setIcon(QIcon(str(icon_path.resolve())))
    tray.setToolTip("Cabra de pánico — clic para el grito")

    def on_activated(reason: QSystemTrayIcon.ActivationReason) -> None:
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            play_cabra()

    tray.activated.connect(on_activated)

    menu = QMenu()
    act_play = QAction("Reproducir", menu)
    act_play.triggered.connect(play_cabra)
    menu.addAction(act_play)
    menu.addSeparator()
    act_quit = QAction("Salir", menu)
    act_quit.triggered.connect(app.quit)
    menu.addAction(act_quit)
    tray.setContextMenu(menu)

    tray.show()
    if not tray.isVisible():
        QMessageBox.warning(
            None,
            "Cabra de pánico",
            "El icono de bandeja no está visible. Revisa la flecha ^ de iconos ocultos.",
        )

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
