/**
 * Created by lenovo on 2017/12/14.
 */
xo = 'alex';

function Func(){
    var xo = "seven";
    function inner(){
        var xo = 'alvin';
        console.log(xo);
    }
    inner();
}
Func();