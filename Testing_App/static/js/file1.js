//var x=20,y=30;
//alert(x);
//console.log(y);
//console.log(text);
    //var a = Number(prompt("Введіть перше число:"));
    //var b = Number(prompt("Введіть друге число:"));
    //var c = prompt("Введіть дію:");
    //var res = Number(0)
//if (c == "+"){
//    console.log(`${a}+${b}=${Number(a)-Number(b)}`)
//}
//else if (c == "-"){
//    console.log(`${a}-${b}=${a-b}`)
//}
//else if (c=="*"){
//    console.log(`${a}*${b}=${a*b}`)
//}
//else if (c=="/"){
//    console.log(`${a}/${b}=${a/b}`)
//}
//    res = c == "+" ? a+b : c == "-"? a-b : c == "*" ? a*b : c == "/"? a/b:
//    console.log(res);
//var a = Number(prompt("Введіть рік:"));
//var year;
//year = a%4 == 0 ? `рік ${a} є високосним` :  `рік ${a} не є високосним`
//console.log(year);
//if (a % 400 ==0 || a % 4 !=0){
//console.log("Цей рік не є викосним");
//}
//else {
//console.log("Цей рік є викосним");
//}

//let a=0, b=0;
//while(a<=10){
//b+=a;
//a++;
//}
//console.log(b)


//СУМА ПАРНИХ ЧИСЕЛ ВІД 0 ДО 100
//var s=0
//for (let i=0; i<100;i++){
//if (i%2==0){
//s+=i;
//}
//else continue
//}
//console.log(s)

//СОРТУВАННЯ БУЛЬБАШКОЮ
//let list = [4,2,6,34,6,34,6,2,6,47,3,36,8,2,62,46,357,975,243,7,24,6,12463,5,21,3,12,3,2,53,5];
//for (let i1=0; i1<list.length; i1++){
//        for (let i=0; i<(list.length-1); i++){
//                if (list[i] < list[i+1] || list[i] == list[i+1]){
//                continue
//            }
//            else {
//                var temp=list[i];
//                list[i]=list[i+1];
//                list[i+1]=temp;
//            }
//        }
//}
//console.log(list);


//var db = {};
//while (true){
//    var name = String(prompt("Введіть ім'я"));
//    var password = String(prompt("Введіть пароль"));
//    if (name=="Stop" || password=="Stop"){
//        var check_name = String(prompt("Введіть ім'я користувача, якого хочете знайти в базі даних"));
//        var check_password = String(prompt("Введіть пароль користувача, якого хочете знайти в базі даних"));
//        if (db[[check_name,check_password]] != null){
//            console.log(`Знайдено користувача з іменем ${check_name} і паролем ${check_password}`);
//        }
//        else{
//            console.log(`Не знайдено користувача з іменем ${check_name} і паролем ${check_password}`);
//    }
//    }
//    else{
//    db[[name,password]] = ("new_user");
//    }
//}


function action(arr,act){
        if (act == "max"){
            max=arr[0];
            for(let j of arr){
            if (j>max){
            max=j;
            }
            }
            console.log(max);
        }
        else if(act == "min"){
            min=arr[0];
            for(let j of arr){
            if (j<min){
            min=j;
            }
            }
            console.log(min);
            }
        else if(act == "avg"){
            var sum;
            for(let j of arr){
            sum+=j;
            }
            console.log(sum/arr.length);
            }
        else if(act == "sum"){
            var sum;
            for(let j of arr){
            sum+=j;
            }
            console.log(sum);
            }
        }

var val1 = prompt("Введіть перше значення");
var val2 = prompt("Введіть друге значення");
var val3 = prompt("Введіть третє значення");
var val4 = prompt("Введіть четверте значення");
var act = prompt("Введіть дію");
array=[val1,val2,val3,val4];
action(array,act);