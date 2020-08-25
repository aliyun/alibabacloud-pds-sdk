// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 批处理
     */
    public class BatchRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// Requests 请求合集
        /// </summary>
        [NameInMap("requests")]
        [Validation(Required=true)]
        public List<BatchSubRequest> Requests { get; set; }

        /// <summary>
        /// 支持的资源类型
        /// </summary>
        [NameInMap("resource")]
        [Validation(Required=true)]
        public string Resource { get; set; }

    }

}
