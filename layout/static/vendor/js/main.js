const upload_img_box = document.querySelector('.upload_img_box');
const selectedImage = document.querySelector('#selectedImage');
const choose_image = document.querySelector('.choose_image');

const image_holder = document.querySelector('.image_holder');
const image = document.querySelector('#image');

const clearAll = document.querySelector('#clearAll');
const remove_img_btn = document.querySelector('#remove_img_btn');

const canvas = document.querySelector('#image_canvas');
const context = canvas.getContext('2d');

let File_Name;
let Edited = false;

/*handle choose image event*/
upload_img_box.addEventListener("click", function () {
   selectedImage.click();
});

/*choose image event*/
selectedImage.addEventListener("change", function () {
   const file = this.files[0];

   if (file) {
      const reader = new FileReader();
      File_Name = file.name;

      choose_image.style.display = "none";
      image_holder.style.display = "block";

      reader.addEventListener("load", function () {
         image.setAttribute("src", this.result);
      });

      reader.readAsDataURL(file);
      remove_img_btn.style.display = "block";
   }

   if (Edited == false) {
      Edited = true;
   }
})

/*download image btn click*/
function Download_btn() {

   if (image.getAttribute('src') != "") {

      if (Edited == true) {
         context.drawImage(image, 0, 0, canvas.width, canvas.height);
         var jpegUrl = canvas.toDataURL("image/jpg");

         const link = document.createElement("a");
         document.body.appendChild(link);

         link.setAttribute("href", jpegUrl);
         link.setAttribute("download", File_Name);
         link.click();
         document.body.removeChild(link);

      }
   }
}

/*remove image btn click*/
remove_img_btn.addEventListener("click", function () {
   image.src = "";
   this.style.display = "none";
   choose_image.style.display = "block";
   image_holder.style.display = "none";
})