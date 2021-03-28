const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return `${[year, month, day].map(formatNumber).join('/')} ${[hour, minute, second].map(formatNumber).join(':')}`
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : `0${n}`
}

// Django请求路径的地址
// let DjangoURL='http://127.0.0.1:8000/'
let DjangoURL='http://192.168.43.139:8000/'


module.exports = {
  formatTime,
  DjangoURL
}
