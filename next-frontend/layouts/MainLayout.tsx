const MainLayout = ({ children }: any) => {
    
    return (
        <div className="flex min-h-screen py-12 px-8 sm:px-8 lg:px-8 bg-primaryDark">
            {children}
        </div>
    );
    
}

export default MainLayout