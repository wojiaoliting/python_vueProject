const REQUEST_HOST: string = 'http://localhost:8001';
const PAGE_SIZE: number = 6;
function ChangeImgURLTorellView(htmlStr: string) {
    const str = htmlStr.replace(/<img.*?src=\"(.*?)\"|url\(\'(.*?)\'\)/g,
    (m: any, p1: any, p2: any, p3: any, p4: any): any => {
        if (p1) {
            if (p1.indexOf(REQUEST_HOST) !== -1) {
                return m;
            }
            const s = m.replace(p1, REQUEST_HOST + p1);
            return s;
        } else if (p2) {
            if (p2.indexOf(REQUEST_HOST) !== -1) {
                return m;
            }
            const s = m.replace(p2, REQUEST_HOST + p2);
            return s;
        }
    });
    return str;
}
export default {
    REQUEST_HOST,
    PAGE_SIZE,
    ChangeImgURLTorellView,
};
