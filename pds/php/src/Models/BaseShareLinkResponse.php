<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * list_share_link response.
 */
class BaseShareLinkResponse extends Model
{
    /**
     * @description created_at
     *
     * @example 2006-01-02T15:04:05.999Z
     *
     * @var string
     */
    public $createdAt;

    /**
     * @description 下载次数
     *
     * @example 1
     *
     * @var int
     */
    public $downloadCount;

    /**
     * @description drive_id
     *
     * @example 1
     *
     * @var string
     */
    public $driveId;

    /**
     * @description expiration
     *
     * @example 2006-01-02T15:04:05.999Z
     *
     * @var string
     */
    public $expiration;

    /**
     * @description expired
     *
     * @example false
     *
     * @var bool
     */
    public $expired;

    /**
     * @description file_id
     *
     * @example 5d5b846942cf94fa72324c14a4bda34e81da635d
     *
     * @var string
     */
    public $fileId;

    /**
     * @description preview_count
     *
     * @example 1
     *
     * @var int
     */
    public $previewCount;

    /**
     * @description 转存次数
     *
     * @example 1
     *
     * @var int
     */
    public $saveCount;

    /**
     * @description share_id
     *
     * @example z6e81Up4u3GDBoJ741dm8z8fZBc2dh8gW
     *
     * @var string
     */
    public $shareId;

    /**
     * @description share_msg
     *
     * @example 复制这条消息并打开app，即可跳转到对应的分享页面
     *
     * @var string
     */
    public $shareMsg;

    /**
     * @description share_policy
     *
     * @example url
     *
     * @var string
     */
    public $sharePolicy;

    /**
     * @description share_pwd
     *
     * @example 12ABcd
     *
     * @var string
     */
    public $sharePwd;

    /**
     * @description share_url
     *
     * @example https://www.aliyundrive.com/sharelinks/index/abcdefghi
     *
     * @var string
     */
    public $shareUrl;

    /**
     * @description updated_at
     *
     * @example 2006-01-02T15:04:05.999Z
     *
     * @var string
     */
    public $updatedAt;
    protected $_name = [
        'createdAt'     => 'created_at',
        'downloadCount' => 'download_count',
        'driveId'       => 'drive_id',
        'expiration'    => 'expiration',
        'expired'       => 'expired',
        'fileId'        => 'file_id',
        'previewCount'  => 'preview_count',
        'saveCount'     => 'save_count',
        'shareId'       => 'share_id',
        'shareMsg'      => 'share_msg',
        'sharePolicy'   => 'share_policy',
        'sharePwd'      => 'share_pwd',
        'shareUrl'      => 'share_url',
        'updatedAt'     => 'updated_at',
    ];

    public function validate()
    {
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->createdAt) {
            $res['created_at'] = $this->createdAt;
        }
        if (null !== $this->downloadCount) {
            $res['download_count'] = $this->downloadCount;
        }
        if (null !== $this->driveId) {
            $res['drive_id'] = $this->driveId;
        }
        if (null !== $this->expiration) {
            $res['expiration'] = $this->expiration;
        }
        if (null !== $this->expired) {
            $res['expired'] = $this->expired;
        }
        if (null !== $this->fileId) {
            $res['file_id'] = $this->fileId;
        }
        if (null !== $this->previewCount) {
            $res['preview_count'] = $this->previewCount;
        }
        if (null !== $this->saveCount) {
            $res['save_count'] = $this->saveCount;
        }
        if (null !== $this->shareId) {
            $res['share_id'] = $this->shareId;
        }
        if (null !== $this->shareMsg) {
            $res['share_msg'] = $this->shareMsg;
        }
        if (null !== $this->sharePolicy) {
            $res['share_policy'] = $this->sharePolicy;
        }
        if (null !== $this->sharePwd) {
            $res['share_pwd'] = $this->sharePwd;
        }
        if (null !== $this->shareUrl) {
            $res['share_url'] = $this->shareUrl;
        }
        if (null !== $this->updatedAt) {
            $res['updated_at'] = $this->updatedAt;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return BaseShareLinkResponse
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['created_at'])) {
            $model->createdAt = $map['created_at'];
        }
        if (isset($map['download_count'])) {
            $model->downloadCount = $map['download_count'];
        }
        if (isset($map['drive_id'])) {
            $model->driveId = $map['drive_id'];
        }
        if (isset($map['expiration'])) {
            $model->expiration = $map['expiration'];
        }
        if (isset($map['expired'])) {
            $model->expired = $map['expired'];
        }
        if (isset($map['file_id'])) {
            $model->fileId = $map['file_id'];
        }
        if (isset($map['preview_count'])) {
            $model->previewCount = $map['preview_count'];
        }
        if (isset($map['save_count'])) {
            $model->saveCount = $map['save_count'];
        }
        if (isset($map['share_id'])) {
            $model->shareId = $map['share_id'];
        }
        if (isset($map['share_msg'])) {
            $model->shareMsg = $map['share_msg'];
        }
        if (isset($map['share_policy'])) {
            $model->sharePolicy = $map['share_policy'];
        }
        if (isset($map['share_pwd'])) {
            $model->sharePwd = $map['share_pwd'];
        }
        if (isset($map['share_url'])) {
            $model->shareUrl = $map['share_url'];
        }
        if (isset($map['updated_at'])) {
            $model->updatedAt = $map['updated_at'];
        }

        return $model;
    }
}
