// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 更新文件元数据
     */
    public class UpdateFileMetaRequest : TeaModel {
        /// <summary>
        /// check_name_mode
        /// </summary>
        [NameInMap("check_name_mode")]
        [Validation(Required=false)]
        public string CheckNameMode { get; set; }

        [NameInMap("custom_index_key")]
        [Validation(Required=false)]
        public string CustomIndexKey { get; set; }

        /// <summary>
        /// description
        /// type: string
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false, MaxLength=1024)]
        public string Description { get; set; }

        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=true, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        [NameInMap("encrypt_mode")]
        [Validation(Required=false)]
        public string EncryptMode { get; set; }

        /// <summary>
        /// file_id
        /// </summary>
        [NameInMap("file_id")]
        [Validation(Required=true, MaxLength=50, Pattern="[a-z0-9.-_]{1,50}")]
        public string FileId { get; set; }

        /// <summary>
        /// hidden
        /// type: boolean
        /// </summary>
        [NameInMap("hidden")]
        [Validation(Required=false)]
        public bool? Hidden { get; set; }

        /// <summary>
        /// labels
        /// </summary>
        [NameInMap("labels")]
        [Validation(Required=false)]
        public List<string> Labels { get; set; }

        [NameInMap("meta")]
        [Validation(Required=false)]
        public string Meta { get; set; }

        /// <summary>
        /// name
        /// </summary>
        [NameInMap("name")]
        [Validation(Required=false, MaxLength=1024)]
        public string Name { get; set; }

        /// <summary>
        /// starred
        /// type: boolean
        /// </summary>
        [NameInMap("starred")]
        [Validation(Required=false)]
        public bool? Starred { get; set; }

        /// <summary>
        /// user_meta
        /// </summary>
        [NameInMap("user_meta")]
        [Validation(Required=false)]
        public string UserMeta { get; set; }

    }

}
