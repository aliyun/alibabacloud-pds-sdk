// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * batch operation response
     */
    public class BatchResponse : TeaModel {
        /// <summary>
        /// responses 返回结果合集
        /// </summary>
        [NameInMap("responses")]
        [Validation(Required=false)]
        public List<BatchSubResponse> Responses { get; set; }

    }

}
