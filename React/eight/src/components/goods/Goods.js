import Good from "./Good";
import "./Goods.css"

function Goods({ goods, onChangeCount }) {

    return (
        <div>
            <ul className="default-ul">
                {
                    goods.map((elem) => (
                        <Good
                            key={elem.id}
                            {...elem}
                            onChangeCount={onChangeCount}
                        />
                    ))
                }
            </ul>
            <hr />
        </div>
    )
}

export default Goods;