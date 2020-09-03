// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class BatchSubRequest : TeaModel {
        /// <summary>
        /// body 子请求的请求参数 json 字符串，可参考对于子请求文档, 当指定了body 必须传headers ： "Content-Type" 对应的类型，目前子请求入参是"application/json"
        /// </summary>
        [NameInMap("body")]
        [Validation(Required=false)]
        public Dictionary<string, object> Body { get; set; }

        /// <summary>
        /// headers 请求头，表示body传入数据的类型
        /// </summary>
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, object> Headers { get; set; }

        /// <summary>
        /// id 用于request 和 response关联， 不允许重复
        /// </summary>
        [NameInMap("id")]
        [Validation(Required=true)]
        public string Id { get; set; }

        /// <summary>
        /// method
        /// </summary>
        [NameInMap("method")]
        [Validation(Required=true)]
        public string Method { get; set; }

        /// <summary>
        /// url 子请求的api path路径， 可参考对于子请求文档
        /// </summary>
        [NameInMap("url")]
        [Validation(Required=true)]
        public string Url { get; set; }

    }

}
