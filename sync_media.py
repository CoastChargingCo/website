"""Copy and optimize brand photos/video from Google Drive into assets/media."""
from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'assets' / 'media'
SRC = Path(
    r'G:\My Drive\E-bike Charger\04_Marketing\Brand Assets (logos, colors, fonts)\Photos'
)


def optimize_jpeg(source: Path, dest: Path, width: int = 1400) -> None:
    image = Image.open(source).convert('RGB')
    image.thumbnail((width, width), Image.Resampling.LANCZOS)
    image.save(dest, 'JPEG', quality=85, optimize=True)


def transcode_video(source: Path, dest: Path) -> None:
    subprocess.run(
        [
            'ffmpeg',
            '-y',
            '-i',
            str(source),
            '-an',
            '-c:v',
            'libx264',
            '-pix_fmt',
            'yuv420p',
            '-movflags',
            '+faststart',
            '-vf',
            'scale=1280:-2',
            '-crf',
            '23',
            str(dest),
        ],
        check=True,
        capture_output=True,
    )


def poster_from_video(video: Path, poster: Path) -> None:
    subprocess.run(
        [
            'ffmpeg',
            '-y',
            '-i',
            str(video),
            '-ss',
            '00:00:01',
            '-vframes',
            '1',
            str(poster),
        ],
        check=True,
        capture_output=True,
    )


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f'Source folder not found: {SRC}')

    OUT.mkdir(parents=True, exist_ok=True)

    optimize_jpeg(SRC / 'ebike_sunset.jpg', OUT / 'hero.jpg')
    optimize_jpeg(SRC / 'ebike_rocks.jpg', OUT / 'hero-alt.jpg')

    video_src = SRC / 'IMG_7529.MOV'
    video_dest = OUT / 'community.mp4'
    transcode_video(video_src, video_dest)
    poster_from_video(video_dest, OUT / 'community-poster.jpg')

    print(f'Synced media to {OUT}')


if __name__ == '__main__':
    main()
