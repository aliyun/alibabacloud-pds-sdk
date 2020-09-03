// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 创建文件
     */
    public class CreateFileRequest : TeaModel {
        /// <summary>
        /// addition_data
        /// </summary>
        [NameInMap("addition_data")]
        [Validation(Required=false)]
        public Dictionary<string, object> AdditionData { get; set; }

        [NameInMap("auto_rename")]
        [Validation(Required=false)]
        public bool? AutoRename { get; set; }

        /// <summary>
        /// check_name_mode
        /// </summary>
        [NameInMap("check_name_mode")]
        [Validation(Required=false)]
        public string CheckNameMode { get; set; }

        /// <summary>
        /// content_hash
        /// </summary>
        [NameInMap("content_hash")]
        [Validation(Required=false)]
        public string ContentHash { get; set; }

        /// <summary>
        /// content_hash_name
        /// </summary>
        [NameInMap("content_hash_name")]
        [Validation(Required=false)]
        public string ContentHashName { get; set; }

        /// <summary>
        /// ContentMd5
        /// </summary>
        [NameInMap("content_md5")]
        [Validation(Required=false)]
        public string ContentMd5 { get; set; }

        /// <summary>
        /// ContentType
        /// </summary>
        [NameInMap("content_type")]
        [Validation(Required=false)]
        public string ContentType { get; set; }

        /// <summary>
        /// description
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

        /// <summary>
        /// encrypt_mode
        /// </summary>
        [NameInMap("encrypt_mode")]
        [Validation(Required=false)]
        public string EncryptMode { get; set; }

        /// <summary>
        /// file_id
        /// </summary>
        [NameInMap("file_id")]
        [Validation(Required=false)]
        public string FileId { get; set; }

        /// <summary>
        /// hidden
        /// </summary>
        [NameInMap("hidden")]
        [Validation(Required=false)]
        public bool? Hidden { get; set; }

        [NameInMap("image_media_metadata")]
        [Validation(Required=false)]
        public ImageMediaMetadata ImageMediaMetadata { get; set; }

        /// <summary>
        /// labels
        /// </summary>
        [NameInMap("labels")]
        [Validation(Required=false)]
        public List<string> Labels { get; set; }

        /// <summary>
        /// last_updated_at
        /// </summary>
        [NameInMap("last_updated_at")]
        [Validation(Required=false)]
        public string LastUpdatedAt { get; set; }

        [NameInMap("meta")]
        [Validation(Required=false)]
        public string Meta { get; set; }

        /// <summary>
        /// Name
        /// </summary>
        [NameInMap("name")]
        [Validation(Required=true, MaxLength=1024)]
        public string Name { get; set; }

        /// <summary>
        /// parent_file_id
        /// </summary>
        [NameInMap("parent_file_id")]
        [Validation(Required=true, MaxLength=50, Pattern="[a-z0-9]{1,50}")]
        public string ParentFileId { get; set; }

        /// <summary>
        /// part_info_list
        /// </summary>
        [NameInMap("part_info_list")]
        [Validation(Required=false)]
        public List<UploadPartInfo> PartInfoList { get; set; }

        /// <summary>
        /// pre_hash
        /// </summary>
        [NameInMap("pre_hash")]
        [Validation(Required=false)]
        public string PreHash { get; set; }

        /// <summary>
        /// Size
        /// </summary>
        [NameInMap("size")]
        [Validation(Required=false)]
        public long Size { get; set; }

        /// <summary>
        /// streams_info
        /// </summary>
        [NameInMap("streams_info")]
        [Validation(Required=false)]
        public Dictionary<string, object> StreamsInfo { get; set; }

        /// <summary>
        /// Type
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=true)]
        public string Type { get; set; }

        /// <summary>
        /// user_meta
        /// </summary>
        [NameInMap("user_meta")]
        [Validation(Required=false)]
        public string UserMeta { get; set; }

        [NameInMap("video_media_metadata")]
        [Validation(Required=false)]
        public VideoMediaMetadata VideoMediaMetadata { get; set; }

    }

}
