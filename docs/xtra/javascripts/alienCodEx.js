/**Automatically set the widht of the canvas */
function p5canvasAutoWidthAndAdmonitions(canvas, dynamicDrawFlag, largeur, hauteur, target){

    // Fix the width so that the image always fit the outer admonition/container.
    const C = $(canvas.elt)
    C.css({
        width: `min( 100% , ${largeur}px )`,
        height: '100%',
    })

    // Make sure the `p5.draw` event loop is deactivated when the admonitions/details are closed.
    //  - Does nothing if no details parent.
    //  - works at any details depth.
    const jDetails = C.parents('details')
    const details  = [...jDetails]
    const drawable =(_="")=>{
        const yup = details.every( d=>d.getAttribute('open')!==null )
        // console.log(`${ target } ${ _ }`, yup)
        return yup
    }

    // Setup reactivity (Call delayed to next tic, otherwise the attributes are not yet up to date):
    jDetails.find("summary").on('click', function(){
        setTimeout(_=> dynamicDrawFlag[0]=drawable() )
    })

    // Properly initialize the state:
    dynamicDrawFlag[0] = drawable('init')
}