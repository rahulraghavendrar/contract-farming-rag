import { useState } from "react";
import api from "../services/api";

function UploadBox() {

    const [file, setFile] = useState(null);

    const uploadFile = async () => {

        if (!file) {
            alert("Select a PDF");
            return;
        }

        const formData = new FormData();

        formData.append(
            "file",
            file
        );

        try {

            const response = await api.post(
                "/upload",
                formData
            );

            alert(
                response.data.message
            );

        } catch (error) {

            console.log(error);

            alert(
                "Upload Failed"
            );
        }
    };

    return (

        <div>

            <h2>Upload PDF</h2>

            <input
                type="file"
                onChange={(e) =>
                    setFile(
                        e.target.files[0]
                    )
                }
            />

            <button
                onClick={uploadFile}
            >
                Upload
            </button>

        </div>
    );
}

export default UploadBox;
