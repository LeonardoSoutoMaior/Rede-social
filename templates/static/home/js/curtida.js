function curtirPublicacao(publicacao_id) {
    const csrftoken = getCookie('csrftoken');
    const url = `/home/curtir_publicacao/${publicacao_id}/`;
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Atualizar a interface do usuário com o número de curtidas e o estado do botão
        const curtidasElement = document.getElementById(`curtidas-publicacao-${publicacao_id}`);
        const curtirButton = document.getElementById(`curtir-button-${publicacao_id}`);
        if (data.curtido) {
            curtirButton.textContent = 'Descurtir';
        } else {
            curtirButton.textContent = 'Curtir';
        }
        curtidasElement.textContent = data.curtidas;
    })
    .catch(error => console.error('Error:', error));
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}