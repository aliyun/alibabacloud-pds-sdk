// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 获取文件夹size信息
     */
    public class GetDirSizeInfoResponse : TeaModel {
        /// <summary>
        /// dir_count
        /// </summary>
        [NameInMap("dir_count")]
        [Validation(Required=false)]
        public long? DirCount { get; set; }

        /// <summary>
        /// file_count
        /// </summary>
        [NameInMap("file_count")]
        [Validation(Required=false)]
        public long? FileCount { get; set; }

        /// <summary>
        /// size
        /// </summary>
        [NameInMap("size")]
        [Validation(Required=false)]
        public long? Size { get; set; }

    }

}
