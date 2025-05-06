from PIL import Image

def resize_image_to_match(input_image_path, reference_image_path, output_image_path):
    """
    将输入图片调整为参考图片的大小并保存。
    
    :param input_image_path: 输入图片的路径
    :param reference_image_path: 参考图片的路径（用于获取目标大小）
    :param output_image_path: 输出图片的路径
    """
    try:
        # 打开输入图片和参考图片
        input_image = Image.open(input_image_path)
        reference_image = Image.open(reference_image_path)
        
        # 获取参考图片的大小
        target_size = reference_image.size
        
        # 调整输入图片的大小
        resized_image = input_image.resize(target_size, Image.Resampling.LANCZOS)
        
        # 保存调整大小后的图片
        resized_image.save(output_image_path)
        print(f"图片已成功调整大小并保存为 {output_image_path}")
    except Exception as e:
        print(f"处理图片时发生错误: {e}")

# 示例用法
input_image_path = r"D:\1111training_code\个人网页\responsive-portfolio-website-master\assets\img\ai_before.png"  # 替换为第一张图片的路径
reference_image_path = r"D:\1111training_code\个人网页\responsive-portfolio-website-master\assets\img\raicom.jpg"  # 替换为第二张图片的路径
output_image_path = r"D:\1111training_code\个人网页\responsive-portfolio-website-master\assets\img\ai.png"  # 替换为保存路径

resize_image_to_match(input_image_path, reference_image_path, output_image_path)