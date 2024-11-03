from PIL import Image
import pillow_avif  # 確保 avif 支援被加載
import io
import os

os.system('cls')

def resize_and_convert_image(input_path, target_width=360, max_size_kb=300):
    # 確認輸入的檔案存在
    if not os.path.isfile(input_path):
        print("指定的檔案不存在。請檢查路徑。")
        return

    # 開啟圖片
    with Image.open(input_path) as img:
        # 計算新高度 (等比縮放)
        width_percent = target_width / float(img.width)
        target_height = int((float(img.height) * float(width_percent)))

        # 調整圖片尺寸
        img_resized = img.resize((target_width, target_height), Image.LANCZOS)

        # 逐步嘗試降低品質以達到目標大小
        quality = 95  # 初始品質設定
        while quality > 10:
            # 暫存到記憶體，並檢查檔案大小
            with io.BytesIO() as buffer:
                img_resized.save(buffer, format="JPEG", quality=quality)
                size_kb = buffer.tell() / 1024  # 取得 KB 單位的大小
                
                # 如果符合條件就儲存並退出
                if size_kb <= max_size_kb:
                    # 生成輸出檔案的路徑
                    base, ext = os.path.splitext(input_path)
                    output_path = f"{base}_{target_width}x{target_height}.jpg"
                    
                    with open(output_path, "wb") as f:
                        f.write(buffer.getvalue())
                    print(f"圖片已儲存至 {output_path}，大小為 {size_kb:.2f} KB")
                    return

            # 每次降低品質後再試
            quality -= 5

    print("無法在要求的大小限制下保存圖片。")

# 使用範例
input_image_path = input("請輸入圖檔的完整路徑：")
resize_and_convert_image(input_image_path)
