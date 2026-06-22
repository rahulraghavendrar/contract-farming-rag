import { useState } from "react";
import api from "../services/api";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function ChatBox() {

    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    const askQuestion = async () => {

        if (!question) {
            return;
        }

        try {

            const response = await api.post(
                "/chat",
                {
                    question
                }
            );

            setAnswer(
                response.data.answer
            );

        } catch (error) {

            console.log(error);

            alert(
                error.response?.data?.detail ||
                error.message
            );
        }
    };

    return (

        <div>

            <h2>Ask Question</h2>

            <input
                value={question}
                onChange={(e) =>
                    setQuestion(
                        e.target.value
                    )
                }
                placeholder="Ask a question"
            />

            <button
                onClick={askQuestion}
            >
                Ask
            </button>

            <h3>Answer</h3>

            <ReactMarkdown
                remarkPlugins={[remarkGfm]}
            >
                {answer}
            </ReactMarkdown>

        </div>
    );
}

export default ChatBox;