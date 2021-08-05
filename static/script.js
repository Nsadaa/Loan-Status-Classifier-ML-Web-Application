
function view_function(){ window.location="C:/Users/SADARUWAN/PycharmProjects/Loan_Status_Classifier/templates/form.html"; }

function clear_function(){

    document.getElementById("form").reset();
}

function back_function(){ window.location="C:/Users/SADARUWAN/PycharmProjects/Loan_Status_Classifier/templates/index.html"; }


function validation(){
    var loan_amount = document.getElementById("loanamount");

    if (loan_amount.value.trim() == "" )
    {
        alert("Loan Amount Is Empty")
        return false;
    }

    else
    {
        true;
    }
}