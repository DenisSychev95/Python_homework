import "./Header.css"

function Header(props) {
    let { group, album} = props

    return (
        <div className="Head">
            <h1>{group}</h1>
            <h2>{album}</h2>
            
        </div>
    )
}

export default Header;