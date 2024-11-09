import "@typespec/http";
//import "@typespec/rest";
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
   v0, "v0.1",
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

// @get op listEmployees(@query size?: int8 , @query page:int8,
// @query({format: "csv"}) csv?: string[], ) : Employee[]; 
// @get op getEmployee(@path empId : int32) : Employee; 
    
@post op createEmployee(@body emp : Employee, @header xApiKey : string) : Employee;
    
// @get 
// @route("/status")
//  op getStatus() : string; 
    
model Employee {
    @maxLength(50)
    @minLength(10)
    name : string; 
    fName : string; 
    lName : string; 
    age : int8; 
    sex : "F" | "M"; 
}
    

