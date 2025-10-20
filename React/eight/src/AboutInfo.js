import { useParams, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";

function AboutInfo() {
    let { id } = useParams();
    let [post, setPost] = useState(null);
    let navigate = useNavigate();
    useEffect(() => {
        fetch(`https://jsonplaceholder.typicode.com/posts/${id}`)
            .then(response => response.json())
            .then(data => setPost(data))

    }, [id])

    let goBack=()=> navigate(-1);
    return (
        <div className="content">
            {
                post && (
                    <>
                        <h1>{post.title}</h1>
                        <p>{post.body}</p>
                        <button onClick={goBack}>Назад</button>
                    </>
                )
            }
        </div>
    )
}

export default AboutInfo;