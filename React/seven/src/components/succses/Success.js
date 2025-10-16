import "./Success.css"

function Succses({ count }) {
    return (
        <div className="success-block">
            <h3>Успешно!</h3>
            <p>Всем <b>{count}</b> пользователям отправлено приглашение</p>
            {/* <a href="/">Назад</a> */}
            <button className="send-invite-btn" onClick={()=> window.location.reload()}>Назад</button>
        </div>
    )
}

export default Succses