function asd(inpt) {
  let city = inpt[0];
  let sales = Number(inpt[1]);

  if (sales <= 500) {
    console.log(sales * 0.05);
  } else if (sales > 500 && sales <= 1000) {
    console.log(sales * 0.07);
  } else if (sales > 1000 && sales <= 10000) {
    console.log(sales * 0.08);
  } else {
    console.log(sales * 0.12);
  }
}

asd(["Sofia", 1500]);
