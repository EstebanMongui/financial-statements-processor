class FileManager:
    def read_file(file_path):
        def decorator(fn):
            def wrapper(*args, **kwargs):
                with open(file_path, "r", encoding="utf-8") as file:
                    result = fn(file)
                    return result

            return wrapper

        return decorator

    def writeFile(file_name, path, extension):
        # Todo: implement writeFile(file_path)
        return
