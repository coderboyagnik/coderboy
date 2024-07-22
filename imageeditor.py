from PIL import Image, ImageOps

def apply_grayscale(image_path, output_path):
    image = Image.open(image_path)
    gray_image = ImageOps.grayscale(image)
    gray_image.save(output_path)

def apply_sepia(image_path, output_path):
    image = Image.open(image_path)
    sepia_image = ImageOps.colorize(ImageOps.grayscale(image), '#704214', '#C0C0C0')
    sepia_image.save(output_path)

def main():
    choice = input("Choose filter (grayscale/sepia): ").strip().lower()
    image_path = input("Enter the path to the image: ")
    output_path = input("Enter the output path: ")

    if choice == 'grayscale':
        apply_grayscale(image_path, output_path)
    elif choice == 'sepia':
        apply_sepia(image_path, output_path)
    else:
        print("Invalid choice")

    print("Image processed successfully.")

if __name__ == "__main__":
    main()
