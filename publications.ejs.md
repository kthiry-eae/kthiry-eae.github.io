```{=html}
<div class="list">
<% for (const item of items) { %>
  <article <%= metadataAttrs(item) %>>
    <h3><%- item.title %></h3>
    <p><%- item.authors || "" %></p>
    <p><%- item.venue || "" %> — <%- item.date || "" %></p>
  </article>
<% } %>
</div>
```