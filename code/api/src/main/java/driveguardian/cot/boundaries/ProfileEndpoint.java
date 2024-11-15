package driveguardian.cot.boundaries;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import  driveguardian.cot.entities.User;
import  driveguardian.cot.repositories.UserRepository;

import java.util.function.Supplier;


@ApplicationScoped
@Path("profile") // returns details of the user for the profile page
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class ProfileEndpoint {
    private static final Supplier<WebApplicationException> NOT_FOUND =
            () -> new WebApplicationException(Response.Status.NOT_FOUND);

    @Inject
    private UserRepository repository;

    @GET
    @Path("/{mail}")
    public User get(@PathParam("mail") String username) {
        User user = repository.findById(username).orElseThrow();
        String passwordhash = ""; // create user with empty string  instead of password
        User profile = new User(user.getName(), user.getfullname(), passwordhash, user.getPermissionLevel());
        return profile;

    }
}