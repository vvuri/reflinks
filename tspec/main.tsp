import "@typespec/http";
// import "@typespec/rest";
import "@typespec/openapi3";
import "@typespec/versioning";

using TypeSpec.Http;
using TypeSpec.Versioning;

@service({
    title: "ML Reference Links"
})
@server("https://vvuri.ru", "endpoint for agent reflinks")
@versioned(Versions)
namespace MLRefLinks;

enum Versions {
    v1
}

model Widget {
    @key id: string;
    weight: int32;
    color: "red" | "blue";
  }
  
@error
model Error {
    code: int32;
    message: string;
}
  
// interface WidgetService extends Resource.ResourceOperations<Widget, Error> {
//     @get @route("customGet") customGet(): Widget;
// }


