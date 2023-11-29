from django.http import HttpResponse
from django.template import Template, Context
from buscador.funciones import buscar_palabra,convertir_cadena_a_objetos

def principal(request): # Vista Principal
    doc_palntilla_principal = open("C:/Users/juanm/Programacion/DJANGO/buscador/buscador/plantillas/principal.html")
    plt_principal = Template(doc_palntilla_principal.read())
    doc_palntilla_principal.close()
    ctx_principal = Context()
    barraBusqueda = plt_principal.render(ctx_principal)
    return HttpResponse(barraBusqueda)

def resultados(request):
    busqueda = request.GET.get('busqueda', '')
    resultado = buscar_palabra(busqueda)
    lista_resultados = convertir_cadena_a_objetos(resultado)
    doc_plantilla_resultados = open("C:/Users/juanm/Programacion/DJANGO/buscador/buscador/plantillas/resultados.html")
    plt_resultados = Template(doc_plantilla_resultados.read())
    doc_plantilla_resultados.close()
    ctx_resultados = Context({"lista_resultados": lista_resultados, "resultado": busqueda})
    resultados = plt_resultados.render(ctx_resultados)
    return HttpResponse(resultados)
