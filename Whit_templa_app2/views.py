from django.shortcuts import render, redirect
from books_authors_app.models import Book, Author
from django.db.models import F, CharField, Value as V
from django.db.models.functions import Concat


def index(request):
    #
    if request.method == "GET":
        librosall = Book.objects.all()
        autoresall = Author.objects.all()
        context = {
            'todosloslibros': librosall,
            'todoslosautores': autoresall
        }
        return render(request, 'index.html', context)
    #
    if request.method == "POST":
        print("a POST request is being made from Index")
        valor_titulo = request.POST["title_in"]
        valor_descripcion = request.POST["desc_in"]
        print(valor_titulo, valor_descripcion)
        Book.objects.create(title=valor_titulo, description=valor_descripcion)
        return redirect("/")


def autor (request):
    #
    if request.method == "GET":
        librosall = Book.objects.all()
        autoresall = Author.objects.all()
        context = {
            'todosloslibros': librosall,
            'todoslosautores': autoresall
        }
        return render(request, 'autor.html', context)
    #
    if request.method == "POST":
        print("a POST request is being made from Authors")
        print(request.POST)
        valor_nombre = request.POST["first_in"]
        valor_apellido = request.POST["last_in"]
        valor_notas = request.POST["notes_in"]
        print(valor_nombre, valor_apellido, valor_notas)
        Author.objects.create(first_name=valor_nombre, last_name=valor_apellido, notas=valor_notas)
        return redirect("/autor")


def libroid (request, id_solicitado):
    if request.method == "GET":
        librocontext ={ 
        'titulolibro': Book.objects.get(id=id_solicitado).title ,
        'descripcion': Book.objects.get(id=id_solicitado).description,
        'identiflibro': id_solicitado,
        'autoreslibro': Book.objects.get(id=id_solicitado).authors.all,
        'autores_all': Author.objects.all()
        }
        return render(request, 'libro.html', librocontext)
        #
    if request.method == "POST":
        # print("A post request is been made")
        # print(request.POST)
        autorseleccionado = request.POST["addautor"]
        this_book = Book.objects.get(id=id_solicitado)
        contenido = Author.objects.annotate(f_name=Concat('first_name',V(' '), 'last_name',output_field=CharField()))
        for i in range(len(contenido)):
            this_autor = contenido[i].f_name
            if this_autor == autorseleccionado:
                print(this_autor," dice hola a ",autorseleccionado)
                this_book.authors.add(contenido[i])
        return redirect(f"/libro/{id_solicitado}")


def autorid (request, id_solicitado):
    if request.method == "GET":
        autoridcontext ={ 
        'nombreautorlibro': Author.objects.get(id=id_solicitado).first_name,
        'apellidoautorlibro': Author.objects.get(id=id_solicitado).last_name,
        'notas': Author.objects.get(id=id_solicitado).notas,
        'identifautor': id_solicitado,
        'librosautor': Author.objects.get(id=id_solicitado).books.all,
        'libros_all': Book.objects.all()
        }
        return render(request, 'autorid.html', autoridcontext)
    #
    if request.method == "POST":
        #print("A post request hecha desde autorid")
        #print(request.POST)
        libroselected = request.POST["addlibro"]
        este_autor = Author.objects.get(id=id_solicitado)
        for libro in Book.objects.all():
            if libro.title == libroselected:
                print(este_autor," dice hola a ",libroselected)
                este_autor.books.add(libro)
        return redirect(f"/autor/{id_solicitado}")


def borrarautorid (request, id_solicitado):
    borrar = Author.objects.get(id=id_solicitado)
    borrar.delete()
    return redirect("/autor")


def borrarlibroid (request, id_solicitado):
    borrarl = Book.objects.get(id=id_solicitado)
    borrarl.delete()
    return redirect("/")