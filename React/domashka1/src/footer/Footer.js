import "./Footer.css"

function Footer(props) {
    let { released, studio } = props
    return (
        <div className="Last">
            <h4>Released {released}</h4>
            <h5>{studio}</h5>
        </div>
    )
}
export default Footer;