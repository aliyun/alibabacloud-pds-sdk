// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 下载限速配置
     */
    public class RateLimit : TeaModel {
        [NameInMap("part_size")]
        [Validation(Required=false)]
        public long? PartSize { get; set; }

        [NameInMap("part_speed")]
        [Validation(Required=false)]
        public long? PartSpeed { get; set; }

    }

}
