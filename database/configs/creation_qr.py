import os
import qrcode

input_file = "vless.txt"

conf_dir = "./conf"
png_dir = "./png"

os.makedirs(conf_dir, exist_ok=True)
os.makedirs(png_dir, exist_ok=True)

with open(input_file, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

for i, config in enumerate(lines, start=1):
    conf_path = os.path.join(conf_dir, f"{i}.conf")
    with open(conf_path, "w", encoding="utf-8") as cf:
        cf.write(config + "\n")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(config)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    png_path = os.path.join(png_dir, f"{i}.png")
    img.save(png_path)

print(f"Готово! Создано {len(lines)} конфигов и QR-кодов")

