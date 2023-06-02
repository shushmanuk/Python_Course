class OnesThreesNines{
  constructor(x){
    this.x = x;
  };
  
  get ones(){
    return this.x
  };
  get threes(){
    return Math.floor(this.x/3)
  };
  get nines(){
    return Math.floor(this.x/9)
  };
};

let g = new OnesThreesNines(5);
console.log(g.ones);
console.log(g.threes);
console.log(g.nines);