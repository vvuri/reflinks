import "@typespec/http";
import "@typespec/openapi3";
import "@typespec/versioning";

using TypeSpec.Http;
using TypeSpec.Versioning;

enum Versions {
    v0, "v0.1",
}

@error
model Error {
    code: int32;
    message: string;
}

@service({
    title: "ML Reference Links"
})
@server("https://vvuri.ru", "endpoint for agent reflinks")
@versioned(Versions)

@route("/api")
namespace MLRefLinks {

    op GetByIdResource<T>(@path id: int32): T;

    model IdNameDesc extends NameDesc{
        @doc("id of the name")
        id: int32;
    }

    model NameDesc{
        @doc("the name of the name")
        name: string;
        @doc("short descriptio of name")
        description: string;
    }

    interface CRUDOperations<T> {
        op list(): T[];
        op getbyid is GetByIdResource<T>;
        @post op update(@path id: int32, item: NameDesc): T;
    }

    @route("/agents")
    namespace Agents {
        model Agent extends IdNameDesc {};

        interface agent extends CRUDOperations<Agent> {};
    };

    @route("/users")
    namespace Users {
        model User extends IdNameDesc {};

        op getbyid is GetByIdResource<User>;
    };

};
