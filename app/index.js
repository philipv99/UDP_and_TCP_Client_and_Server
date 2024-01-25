const api = "https://localhost:7086/api/KeyBoard" // to get by Id add: "/{id}"


Vue.createApp({
   data(){
      return{
         CO2Log: [
            {id: 1, ppm: 200},
            {id: 3, ppm: 3834},
            {id: 2, ppm: 5467},
         ],
         SortLog: [],

         newLog: {
            id: null,
            ppm: null
         }
      }
      },
      async created(){
         this.CreateSortLog()
      },
      methods: {
         AddLog(){
            this.CO2Log.push(this.newLog)
            this.newLog = {id: null, ppm: null}
         },
         CreateSortLog(){
            this.SortLog = [...this.CO2Log]
         },
         Limit(){
            this.SortLog.forEach( i => {
               if (i[ppm] < 1000){
                  index = this.SortLog.indexof(i)
                  this.SortLog.splice(index, 1)
               }
            })
         },
         Sort(){
            this.SortLog.sort((a, b ) => {
               return (b.ppm - a.ppm)
            })
         }
   }
}).mount("#app")