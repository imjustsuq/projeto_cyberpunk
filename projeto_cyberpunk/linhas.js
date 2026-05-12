document.querySelector('#typing')
const linhas = [
    document.getElementById("linha1"),
    document.getElementById("linha2"),
    document.getElementById("linha3"),
    document.getElementById("linha4")
]
const messages = [
    'Projeto Cyberpunk',
    'initializing system...',
    'access granted',
    'welcome, user'
]
let messageIndex = 0
let characterIndex = 0
let currentMessage = ''
let currentCharacter = ''
const type = () => {
    // const shouldTypeFirstMessage = messageIndex === messages.length
    if (messageIndex === messages.length) {
        messageIndex = 0
        characterIndex = 0
        for (let i = 0; i < linhas.length; i++) {
            linhas[i].textContent = ''
        }
        return
    }
    currentMessage = messages[messageIndex]
    currentCharacter = currentMessage.slice(0, characterIndex++)
    linhas[messageIndex].textContent = currentCharacter
    const shouldChangeMessageToBeTyped =
        currentCharacter.length === currentMessage.length

    if (shouldChangeMessageToBeTyped) {
        messageIndex++
        characterIndex = 0
    }
}
setInterval(type, 200)

