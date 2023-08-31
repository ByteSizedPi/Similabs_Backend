import cors from "cors";
import express, { Express } from "express";
import morgan from "morgan";

const app: Express = express();

app.use([
  express.json(),
  cors({
    origin: "http://localhost:4200",
    methods: ["GET", "POST", "DELETE", "PUT"],
    credentials: true,
  }),
  morgan("dev"),
]);
