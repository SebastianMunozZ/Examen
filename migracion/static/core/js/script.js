/*Script para obtener regiones y comunas por API*/
let regiones = []
let comunas = []
const setcomunas = (region)=>{
    //console.log(region,regiones)
    let id
    for(let i=0;i<regiones.length;i++){
        if(region===regiones[i].nombre){
            id = regiones[i].codigo
            break
        }
    }
    let data = []
    for(let i=0;i<comunas.length;i++){
        let cod = comunas[i].codigo
        //console.log(id)
        if(id===comunas[i].codigo.substr(0,2)){
            data.push(comunas[i])
        }
    }
    //console.log(data)
    //data = data.join('')
    let options = data.map((item)=>{return `<option value="${item.nombre}">${item.nombre}</option>`})
    options = options.join('')
    //console.log(options)
    let select = `<select class="form-select" id="validationDefault04" name="cars" id="cars" form="carform">${options}</select>`
    document.getElementById('comunas').innerHTML = select
}

const localidades = async()=>{
    
  fetch('https://apis.digital.gob.cl/dpa/regiones/')
  .then(response => response.json())
  .then((data) =>{ //console.log(data)
      let options = data.map((item)=>{return `<option value="${item.nombre}">${item.nombre}</option>`})
      options = options.join('')
      //console.log(options)
      let select = `<select class="form-select" id="validationDefault04" onchange='setcomunas(this.value)' name="cars" id="cars" form="carform"><option selected disabled value="">Elige tu región</option>${options}</select>`
      //console.log('cargada regiones')
      document.getElementById('region').innerHTML = select
      //console.log('regiones cargadas')
      regiones = data
  });

  fetch(`https://apis.digital.gob.cl/dpa/comunas`)
  .then(response => response.json())
  .then((data) =>{ //console.log(data)
      //console.log('cargadas comuna')
      comunas = data
  });

}
localidades()
/*FIN Script para obtener regiones y comunas por API*/

