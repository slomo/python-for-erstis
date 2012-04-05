var a = [9,8,7,6,5,4,3,2,1,0];

for(var i=0; i<a.length;i++) {
    for(var j=1;j<a.length-i;j++) {
        if(a[j-1] > a[j]) {
            //swap the shit
            var t = a[j-1];
            a[j-1] = a[j];
            a[j] = t;
        }
    }
}

console.log(a);
