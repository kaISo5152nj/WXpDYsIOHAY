# 代码生成时间: 2025-09-23 13:57:39
import tornado.ioloop
import tornado.web
import hashlib
import json

"""
哈希值计算工具Tornado Web应用
"""

class MainHandler(tornado.web.RequestHandler):
    """
    主处理器，提供哈希值计算功能
    """
    def post(self):
        # 获取请求数据
        data = self.get_argument('data')
        try:
            # 计算哈希值
            hash_value = self.calculate_hash(data)
            # 返回结果
            self.write(json.dumps({'hash': hash_value}))
        except Exception as e:
            # 错误处理
            self.write(json.dumps({'error': str(e)}))

    def calculate_hash(self, data):
        """
        计算给定数据的哈希值
        
        Args:
            data (str): 需要计算哈希值的字符串
        
        Returns:
            str: 计算得到的哈希值
        """
        # 使用sha256算法计算哈希值
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()

def make_app():
    """
    创建Tornado Web应用
    """
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    print('Hash Calculator is running on http://localhost:8888')
    tornado.ioloop.IOLoop.current().start()