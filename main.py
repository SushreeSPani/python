from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from rembg import remove
import uuid

app = FastAPI(title="Remove Background")

@app.post("/remover")
async def remove_background(image: UploadFile):
    # Read the uploaded file
    input_data = await image.read()

    # Remove background
    output_data = remove(input_data)

    # Generate a unique filename for the output image
    output_filename = f"{uuid.uuid4()}.png"
    
    # Save the output to a file
    with open(output_filename, "wb") as output_file:
        output_file.write(output_data)

    # Return the file as a response
    return FileResponse(output_filename, media_type="image/png", filename=output_filename)

    # Optionally, clean up the file after returning it
    # os.remove(output_filename)
