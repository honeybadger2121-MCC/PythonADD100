import os

def main():
    # Define the main directory and subdirectories
    main_dir = "MyFiles"
    sub_dirs = ["Docs", "Images", "Videos"]

    try:
        # Create the main directory
        os.mkdir(main_dir)
        print(f"Created directory: {main_dir}")

        # Create subdirectories inside the main directory
        for sub in sub_dirs:
            sub_path = os.path.join(main_dir, sub)
            os.mkdir(sub_path)
            print(f"Created subdirectory: {sub_path}")

    except FileExistsError:
        print("One or more directories already exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
main()
