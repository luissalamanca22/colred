
# def xstr(s):
#     if s is None:
#         return ''
#     try:
#         return s.encode("utf-8")
#     except:
#         return str(s)
#
#

def generate_pdf():
    from reportlab.lib.colors import HexColor
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.units import cm

    path_pdf = "assets/tarjeta_recaudo.pdf"
    path_img_bg = "assets/tarjeta_recaudo_bg.png"
    path_img_barcode = "assets/tarjeta_recaudo_barcode.png"

    PAGE_WIDTH = 240
    PAGE_HEIGHT = 162

    canvas = Canvas(path_pdf)
    canvas.setPageSize((PAGE_WIDTH, PAGE_HEIGHT))
    canvas.setFont('Helvetica', 3)

    #Draw background image
    canvas.drawImage(path_img_bg, x=0, y=0, width=PAGE_WIDTH, height=PAGE_HEIGHT)

    #Draw barcode image
    canvas.drawImage(path_img_barcode, x=15, y=45, width=215, height=52)

    #Set this to True to show the grid
    SHOW_GRID = False

    if SHOW_GRID:
        n = 5
        s = 200
        canvas.setFillColorRGB(0,0,1)
        canvas.setFont('Helvetica',1)
        for x in range(s):
            for y in range(s):
                canvas.rect(x*n,y*n, width=n, height=n, stroke=1)
                canvas.drawString(x*n,y*n,"%s,%s" % ((x*n),(y*n)) )

    canvas.showPage()
    canvas.save()


if __name__ == '__main__':
    generate_pdf()