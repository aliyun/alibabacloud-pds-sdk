// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class BatchSubResponse : TeaModel {
        /// <summary>
        /// body 子请求的返回结果，可参考对于子请求文档 json 字符串
        /// </summary>
        [NameInMap("body")]
        [Validation(Required=false)]
        public Dictionary<string, object> Body { get; set; }

        /// <summary>
        /// id 请求带过来的id, 可以跟 request 进行关联
        /// </summary>
        [NameInMap("id")]
        [Validation(Required=false)]
        public string Id { get; set; }

        /// <summary>
        /// status 子请求的返回状态码，可参考对于子请求文档
        /// </summary>
        [NameInMap("status")]
        [Validation(Required=false)]
        public long Status { get; set; }

    }

}
