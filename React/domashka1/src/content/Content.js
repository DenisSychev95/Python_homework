import "./Content.css"

function Content(props){
    let {songs} = props
    let blank = "_blank";
    
    return(
        <ul className="Content">
            {
                songs.map((elem, index)=>{
                    return <li key={index}><a href={elem.link} target={blank}>{elem.name}</a></li>
                })
            }
        </ul>
    )
}

export default Content;