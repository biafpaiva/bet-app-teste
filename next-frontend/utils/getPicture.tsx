export const imageArray = [
    'https://images.unsplash.com/photo-1495360010541-f48722b34f7d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8Y2F0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
    'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8Y2F0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=400&q=60',
    'https://images.unsplash.com/photo-1543852786-1cf6624b9987?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fGNhdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60',
    'https://images.unsplash.com/photo-1513245543132-31f507417b26?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDB8fGNhdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60',
    'https://images.unsplash.com/photo-1606225457115-9b0de873c5db?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDV8fGNhdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=400&q=60'
];
  
export function getPicture() {
    const random_index = Math.floor(Math.random() * imageArray.length);
    const selected_image = imageArray[random_index];
    return selected_image
}
  