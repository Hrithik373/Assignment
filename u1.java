import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

@SpringBootApplication
public class ShortenerApiApplication {
    public static void main(String[] args) {
        SpringApplication.run(ShortenerApiApplication.class, args);
    }
}

@Controller
class ShortenerController {
    private final Map<String, String> urls = new HashMap<>();

    @PostMapping("/shorten")
    public ResponseEntity<?> shortenUrl(@RequestBody Map<String, String> body, @RequestHeader("Host") String host) {
        String longUrl = body.get("url");
        String shortId = UUID.randomUUID().toString().substring(0, 7);
        String shortUrl = "http://" + host + "/" + shortId;
        urls.put(shortId, longUrl);
        return new ResponseEntity<>(Map.of("short_url", shortUrl), HttpStatus.OK);
    }

    @GetMapping("/{shortId}")
    public ResponseEntity<?> redirectToUrl(@PathVariable String shortId) {
        if (urls.containsKey(shortId)) {
            String longUrl = urls.get(shortId);
            return ResponseEntity.status(HttpStatus.MOVED_PERMANENTLY)
                    .header("Location", longUrl)
                    .build();
        } else {
            return ResponseEntity.status(HttpStatus.NOT_FOUND)
                    .body(Map.of("error", "Short URL not found"));
        }
    }
}